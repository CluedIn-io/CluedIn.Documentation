---
layout: cluedin
title: Building a new Logging Provider
parent: Development
nav_order: 190
has_children: false
permalink: {{ site.baseurl }}/development/building-logging-provider
tags: ["development","logging"]
published: false
---


There is a strong chance that you will have a Logging Provider of choice. CluedIn ships with a few providers, but they might not suit. 

You will need to create a new C# class and inherit from the BaseLoggingTarget. Here is an example below:  

```csharp
namespace CluedIn.Logging.Serilog
{
    public class SerilogLoggingTarget : BaseLoggingTarget
    {
        private readonly ILogger _logger;

        public SerilogLoggingTarget(ILogger logger)
        {
            _logger = logger ?? throw new ArgumentNullException(nameof(logger));
        }

        public override void Write(LogLevel logLevel, DateTimeOffset date, KeyValuePair<string, object>[] contexts, string message, Exception exception = null)
        {

            if (message == null)
            {
                throw new ArgumentNullException(nameof(message));
            }

            _logger.Write(logLevel.ConvertToLogEventLevel(), exception, message);
        }

        public override void Write(LogLine logLine)
        {
            if (logLine == null)
            {
                throw new ArgumentNullException(nameof(logLine));
            }

            var parameters = logLine.ConvertToLogParameters();

            Write(parameters.LogLevel, parameters.Date, parameters.Contexts, parameters.Message, parameters.Exception);
        }
    }
}
```