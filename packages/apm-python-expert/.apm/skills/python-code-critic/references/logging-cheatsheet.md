# Logging Cheatsheet

This document provides examples for adding logging to code in Python and TypeScript.

## Python (Preferred)

```python
import logging

# Configure logging to a file or stream
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# It's good practice to use a logger named after the module
logger = logging.getLogger(__name__)

def complex_function(a, b):
    """
    An example function to demonstrate logging.
    """
    logger.debug(f"Function called with arguments: a={a}, b={b}")
    try:
        result = a / b
        logger.info(f"Calculation successful. Result: {result}")
        if result > 1:
            logger.warning("Result is greater than 1, this might be unexpected.")
        return result
    except ZeroDivisionError as e:
        logger.error("A ZeroDivisionError occurred.", exc_info=True)
        # exc_info=True will add traceback information to the log
        raise
    except Exception as e:
        logger.critical(f"An unexpected critical error occurred: {e}", exc_info=True)
        raise
    finally:
        logger.debug("Exiting complex_function")

# --- Example Usage ---
# complex_function(10, 5)
# complex_function(10, 0)
```

## TypeScript (Fallback)

For Node.js environments, you can use a library like `winston` or `pino` for robust logging. Here is a `winston` example.

**Installation:** `npm install winston`

```typescript
import winston from 'winston';

// Create a logger instance
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp({
      format: 'YYYY-MM-DD HH:mm:ss'
    }),
    winston.format.errors({ stack: true }),
    winston.format.splat(),
    winston.format.json()
  ),
  defaultMeta: { service: 'user-service' },
  transports: [
    // - Write all logs with level `error` and below to `error.log`
    // - Write all logs with level `info` and below to `combined.log`
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' }),
  ],
});

// If we're not in production then log to the `console` with the format:
// `${info.level}: ${info.message} JSON.stringify({ ...rest }) `
if (process.env.NODE_ENV !== 'production') {
  logger.add(new winston.transports.Console({
    format: winston.format.simple(),
  }));
}

function exampleTsFunction(param1: number, param2: number): number {
    logger.debug(`Entering exampleTsFunction with params: ${param1}, ${param2}`);
    if (param2 === 0) {
        logger.error('Division by zero attempted!');
        throw new Error('Cannot divide by zero.');
    }
    const result = param1 / param2;
    logger.info(`Result of division: ${result}`);
    return result;
}

// --- Example Usage ---
// try {
//   exampleTsFunction(10, 2);
//   exampleTsFunction(10, 0);
// } catch (e) {
//   // The error is already logged by the function
// }
```
