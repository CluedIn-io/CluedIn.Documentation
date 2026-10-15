# Agent mode: a Markdown copy of every documentation page, for AI agents.
#
# An agent that fetches an HTML page spends most of its tokens on navigation,
# scripts and markup. This plugin writes, next to every article:
#
#   /<permalink>.md   the article as clean Markdown: a short metadata header,
#                     the body with its Liquid rendered, internal links pointing
#                     at other .md pages, and, on an index page, its children
#   /llms.txt         the entry point (https://llmstxt.org): how the docs are
#                     organised, then every section and subsection with a summary
#   /llms-full.txt    every product page in one file, for bulk loading
#
# Liquid is rendered here, but the Markdown is never converted to HTML. Pages are
# only collected while Jekyll renders them, and the files are written after the
# site, so nothing is added to site.pages and the navigation is unaffected.

require "fileutils"
require "set"

module CluedIn
  module AgentMarkdown
    Doc = Struct.new(:page, :url, :title, :parent, :grand_parent, :nav_order,
                     :content_type, :summary, :has_children, :body, :description)

    module_function

    def docs
      @docs ||= {}
    end

    def reset
      @docs = {}
    end

    # Pages that get a Markdown copy: published Markdown pages with the site's
    # article layout and a title. The home page is a card grid, and llms.txt
    # replaces it. `agent_exclude: true` opts a generated page (such as /tag) out.
    def eligible?(page)
      page.is_a?(Jekyll::Page) &&
        page.site.config["markdown_ext"].to_s.split(",").include?(page.ext.to_s.delete(".")) &&
        page.data["layout"] == "cluedin" &&
        !page.data["title"].to_s.strip.empty? &&
        !page.data["agent_exclude"] &&
        page.url != "/"
    end

    def md_path(url)
      "#{url.chomp("/")}.md"
    end

    def absolute(site, path)
      "#{site.config["url"]}#{site.config["baseurl"]}#{path}"
    end

    def render_liquid(page, payload)
      info = {
        :registers        => { :site => page.site, :page => payload["page"] },
        :strict_filters   => page.site.config.dig("liquid", "strict_filters"),
        :strict_variables => page.site.config.dig("liquid", "strict_variables"),
      }
      page.site.liquid_renderer.file(page.path).parse(page.content).render!(payload, info)
    rescue StandardError => e
      Jekyll.logger.warn "Agent mode:", "Liquid failed in #{page.path} (#{e.message}); using the source"
      page.content
    end

    # Remove what only matters to the HTML theme and rewrite links so an agent
    # that follows one stays on Markdown.
    def clean(site, text, urls)
      text = text.gsub(/\r\n?/, "\n")
      text = text.gsub(/^##+ On this page\s*\n(\{:[^}]*\}\s*\n)?(\s*[-*\d.]+\s*TOC\s*\n)?\{:toc\}\s*\n/i, "")
      text = text.gsub(/^\s*[-*\d.]+\s*TOC\s*\n\{:toc\}\s*\n/, "")
      # A just-the-docs callout is a class on the next paragraph. Keep what it
      # says, so an agent can still tell a warning from a note.
      text = text.gsub(/^\{:\s*\.(note|important|warning|caution|tip|new|highlight)\s*\}[ \t]*\n(?=\S)/) do
        "> **#{Regexp.last_match(1).capitalize}:** "
      end
      text = text.gsub(/^\{:[^}\n]*\}[ \t]*\n/, "")
      text = text.gsub(/\{:\s*[.#][^}\n]*\}/, "")
      # Markup an agent cannot use: embedded viewers, layout wrappers, and
      # HTML links, which become Markdown links so the rewrite below sees them.
      text = text.gsub(%r{<iframe\b.*?</iframe>\s*}m, "")
      text = text.gsub(%r{<a\b[^>]*?href="([^"]+)"[^>]*>(.*?)</a>}m) do
        "[#{Regexp.last_match(2).strip}](#{Regexp.last_match(1)})"
      end
      text = text.gsub(%r{</?(?:p|div|span)\b[^>]*>}, "")
      text = text.gsub(/^[ \t]+$/, "")
      text = text.gsub(/(\]\(|href=")(\/[^)"\s#]*)(#[^)"\s]*)?/) do
        lead, path, anchor = Regexp.last_match(1), Regexp.last_match(2), Regexp.last_match(3)
        key = path.chomp("/")
        key = "/" if key.empty?
        target = urls.include?(key) && key != "/" ? md_path(key) : path
        "#{lead}#{absolute(site, target)}#{anchor}"
      end
      text.gsub(/\n{3,}/, "\n\n").strip
    end

    # The first sentence of the body, for the one-line descriptions in lists.
    def describe(body)
      body.each_line.map(&:strip).each_with_index do |line, _i|
        next if line.empty? || line.start_with?("#", "|", "!", "<", "```", ">", "-", "*", "{")
        next if line =~ /^\d+\./
        text = line.gsub(/!\[[^\]]*\]\([^)]*\)/, "").gsub(/\[([^\]]*)\]\([^)]*\)/, '\1')
                   .gsub(/[*_`]/, "").strip
        next if text.length < 20
        sentence = text[/\A.*?[.!?](?=\s|\z)/] || text
        return sentence.length > 220 ? "#{sentence[0, 217].rstrip}..." : sentence
      end
      nil
    end

    def children_of(doc)
      docs.values
          .select { |d| d.parent == doc.title && d.grand_parent == doc.parent }
          .sort_by { |d| [d.nav_order.to_f, d.title] }
    end

    def top_level
      docs.values.select { |d| d.parent.nil? }.sort_by { |d| [d.nav_order.to_f, d.title] }
    end

    def parent_of(doc)
      return nil unless doc.parent
      docs.values.find do |d|
        d.title == doc.parent && (doc.grand_parent ? d.parent == doc.grand_parent : d.parent.nil?)
      end
    end

    def entry(site, doc)
      type = doc.content_type && doc.content_type != "landing" ? " (#{doc.content_type})" : ""
      text = doc.summary || doc.description
      line = "- [#{doc.title}](#{absolute(site, md_path(doc.url))})#{type}"
      text ? "#{line}: #{text}" : line
    end

    def markdown_for(site, doc)
      types = site.config["content_types"] || {}
      crumbs = [doc.grand_parent, doc.parent].compact
      out = ["---", "title: #{doc.title}", "url: #{absolute(site, doc.url)}"]
      out << "content_type: #{doc.content_type}" if doc.content_type
      out << "section: #{crumbs.join(" > ")}" unless crumbs.empty?
      out << "---" << "" << "# #{doc.title}" << ""
      if doc.content_type && types[doc.content_type] && doc.content_type != "landing"
        out << "> #{doc.content_type}: #{types[doc.content_type]}." << ""
      end
      out << doc.body unless doc.body.empty?

      kids = doc.has_children ? children_of(doc) : []
      unless kids.empty?
        out << "" << "## In this section" << ""
        kids.each { |k| out << entry(site, k) }
      end

      up = parent_of(doc)
      out << "" << "Up: [#{up.title}](#{absolute(site, md_path(up.url))})" if up
      out.join("\n") + "\n"
    end

    # Supporting material, and top-level pages kept out of the sidebar, are
    # listed under "Optional", which llms.txt readers may skip.
    def secondary?(site, doc)
      doc.page.data["nav_exclude"] ||
        doc.nav_order.to_f >= site.config.fetch("nav_secondary_from", 20).to_f
    end

    def llms_txt(site)
      cfg = site.config["agent_mode"] || {}
      out = ["# #{site.config["title"]}", "", "> #{cfg["summary"] || site.config["description"]}", ""]
      out << cfg["instructions"].to_s.strip << "" if cfg["instructions"]
      types = site.config["content_types"] || {}
      out << "Every page declares one content type: " +
             types.reject { |k, _| k == "landing" }.map { |k, v| "#{k} (#{v[0].downcase}#{v[1..]})" }.join(", ") + "."
      out << ""

      primary, optional = top_level.partition { |d| !secondary?(site, d) }
      primary.each do |section|
        out << "## #{section.title}" << ""
        out << entry(site, section)
        children_of(section).each { |kid| out << entry(site, kid) }
        out << ""
      end
      unless optional.empty?
        out << "## Optional" << ""
        optional.each { |section| out << entry(site, section) }
        out << ""
      end
      out.join("\n")
    end

    # Primary sections only, in navigation order, depth first.
    def llms_full(site)
      out = ["# #{site.config["title"]}", ""]
      walk = lambda do |doc|
        out << markdown_for(site, doc).sub(/\A---\n.*?\n---\n\n/m, "<!-- #{absolute(site, doc.url)} -->\n")
        children_of(doc).each { |kid| walk.call(kid) }
      end
      top_level.reject { |d| secondary?(site, d) }.each { |section| walk.call(section) }
      out.join("\n")
    end

    def write(site, path, content)
      dest = File.join(site.dest, path)
      FileUtils.mkdir_p(File.dirname(dest))
      File.write(dest, content)
    end
  end
end

Jekyll::Hooks.register :site, :pre_render do |_site|
  CluedIn::AgentMarkdown.reset
end

Jekyll::Hooks.register :pages, :pre_render do |page, payload|
  next unless CluedIn::AgentMarkdown.eligible?(page)
  # The layout links the Markdown copy (head_custom.html, cluedin.html).
  payload["page"]["agent_markdown"] = CluedIn::AgentMarkdown.md_path(page.url)
  d = page.data
  CluedIn::AgentMarkdown.docs[page.url] = CluedIn::AgentMarkdown::Doc.new(
    page, page.url.chomp("/"), d["title"].to_s, d["parent"], d["grand_parent"], d["nav_order"],
    d["content_type"], d["summary"], d["has_children"],
    CluedIn::AgentMarkdown.render_liquid(page, payload)
  )
end

Jekyll::Hooks.register :site, :post_write do |site|
  m = CluedIn::AgentMarkdown
  urls = m.docs.values.map(&:url).to_set
  m.docs.each_value do |doc|
    doc.body = m.clean(site, doc.body, urls)
    doc.description = m.describe(doc.body)
  end
  m.docs.each_value { |doc| m.write(site, m.md_path(doc.url), m.markdown_for(site, doc)) }
  m.write(site, "llms.txt", m.llms_txt(site))
  m.write(site, "llms-full.txt", m.llms_full(site))
  Jekyll.logger.info "Agent mode:", "#{m.docs.size} Markdown pages, llms.txt, llms-full.txt"
end
