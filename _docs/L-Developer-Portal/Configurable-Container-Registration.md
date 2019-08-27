# Configurable Container Registration

[PR #948](https://github.com/CluedIn-io/CluedIn/pull/948) added the ability to configure search paths for container registrations. For example if a customer wants to include custom assemblies into the container registrations the file prefix can be added to the search patterns list.

Additionally filters is also applied to avoid registrations from unwanted assemblies such as unit test DLLs.

## Change Summary

- Support added for custom assembly filtering such as `[CustomerName].Crawling.[CrawlerName]`.

- A `CluedInTypes` utility class has been added to handle search paths and assembly filtering.

- Existing container installers and registrations updated to use new filter mechanism based on `CluedInTypes`.

- A `ComponentHost.ComponentSearchPatterns` configuration option has been added to support additional component search patterns.

- New component host configuration settings have been added for component containers. The settings will be written to a new `<componentHost />` configuration section in the generated configuration file `ServerComponent - Shared.config`.

### Configuration Settings

| Key | Description | Default |
|-|-|-|
| ComponentHost.ComponentSearchPatterns | Comma separated list of search patterns | "CluedIn.*" |
| ComponentHost.FileExcludes | Comma separated list of exclude patterns |

These settings controls both `ComponentHost` initialization and container registrations.

The standard `CluedIn.*` search pattern will always be included in the search paths no matter what is configured.

Files with the following prefixes will always be filtered: `.Test`, `.Tests`, `.Test.Stubs`

Settings can also be specified using environment variables.

#### Crawler Configuration

Two options are available to support custom assembly filtering prefixes like `[CustomerName].Crawling.[CrawlerName]`:

1. Add the prefix to `ComponentHost.ComponentSearchPatterns` in `app.config`

1. Set the prefix using `CluedInTypes.SearchPatterns` property in test scenarios.
