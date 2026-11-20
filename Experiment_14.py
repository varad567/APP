"""
Experiment 14 - Various uses of the logging module (CO-5)
"""
import logging

# ---------- 1. Basic configuration (console + file) ----------
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log", mode="w"),
        logging.StreamHandler(),
    ],
)

# ---------- 2. All five logging levels ----------
logging.debug("Debug message: detailed information for diagnosing problems")
logging.info("Info message: program is running as expected")
logging.warning("Warning message: something unexpected happened")
logging.error("Error message: a function could not be completed")
logging.critical("Critical message: the program may not continue")

# ---------- 3. Custom named logger with its own handler ----------
logger = logging.getLogger("PaymentModule")
logger.setLevel(logging.INFO)
error_handler = logging.FileHandler("errors.log", mode="w")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(logging.Formatter("%(levelname)s | %(funcName)s | %(message)s"))
logger.addHandler(error_handler)


def process_payment(amount):
    logger.info(f"Processing payment of Rs.{amount}")
    if amount <= 0:
        logger.error(f"Invalid amount: {amount}")
        return False
    logger.info("Payment successful")
    return True


process_payment(500)
process_payment(-20)

# ---------- 4. Logging exceptions with traceback ----------
try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("Exception caught while dividing")

# ---------- 5. Logging variable data ----------
user, attempts = "varad", 3
logging.warning("User %s failed login %d times", user, attempts)

print("\nLogs written to 'app.log' (all) and 'errors.log' (only errors).")
