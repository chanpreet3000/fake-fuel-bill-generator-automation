import json
import logging
import inspect
import os
import traceback
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)


class Logger:
    # Customizable settings
    STORE_TO_FILE = True
    TIMESTAMP_PADDING = 30
    LOG_LEVEL_PADDING = 10
    FILE_PATH_PADDING = 30

    COLORS = {
        'timestamp': Fore.WHITE,
        'debug': Fore.CYAN,
        'info': Fore.GREEN,
        'warning': Fore.YELLOW,
        'error': Fore.RED,
        'critical': Fore.MAGENTA,
        'file_path': Fore.WHITE,
        'details': Fore.LIGHTWHITE_EX
    }

    __console_logger = None
    __file_logger = None

    @staticmethod
    def __setup_loggers():
        if Logger.__console_logger is None:
            # Console logger
            Logger.__console_logger = logging.getLogger(f"{__name__}_console")
            Logger.__console_logger.setLevel(logging.DEBUG)
            console_handler = logging.StreamHandler()
            Logger.__console_logger.addHandler(console_handler)

        if Logger.__file_logger is None and Logger.STORE_TO_FILE:
            # File logger
            Logger.__file_logger = logging.getLogger(f"{__name__}_file")
            Logger.__file_logger.setLevel(logging.DEBUG)
            logs_dir = os.path.join(Logger.get_project_root(), 'logs')
            os.makedirs(logs_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            log_file = os.path.join(logs_dir, f"log-{timestamp}.txt")
            file_handler = logging.FileHandler(log_file)
            file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(file_formatter)
            Logger.__file_logger.addHandler(file_handler)

    @staticmethod
    def get_project_root():
        current_path = os.path.abspath(os.path.dirname(__file__))
        while True:
            if os.path.exists(os.path.join(current_path, 'main.py')):
                return current_path
            parent_path = os.path.dirname(current_path)
            if parent_path == current_path:
                return os.path.abspath(os.path.dirname(__file__))
            current_path = parent_path

    @staticmethod
    def __get_log_details():
        frame = inspect.stack()[3]
        file_name = frame.filename
        line_number = frame.lineno

        project_root = Logger.get_project_root()
        relative_file_name = os.path.relpath(file_name, project_root)
        relative_file_name = f"./{relative_file_name.replace(os.sep, '/')}"

        timestamp = datetime.utcnow().isoformat()
        file_path_info = f"{relative_file_name}:{line_number}"
        return timestamp, file_path_info

    @staticmethod
    def __log(level, message, details, no_meta=False):
        Logger.__setup_loggers()
        timestamp, file_path_info = Logger.__get_log_details()
        level_name = logging.getLevelName(level).lower()

        if no_meta:
            console_log_message = f"{Logger.COLORS[level_name]}{message}"
            file_log_message = f"{message}"
        else:
            console_log_parts = [
                f"{Logger.COLORS['timestamp']}{timestamp:<{Logger.TIMESTAMP_PADDING}}",
                f"{Logger.COLORS[level_name]}{logging.getLevelName(level):<{Logger.LOG_LEVEL_PADDING}}",
                f"{Logger.COLORS['file_path']}{file_path_info:<{Logger.FILE_PATH_PADDING}}",
                f": {Logger.COLORS[level_name]}{message}"
            ]
            console_log_message = " ".join(console_log_parts)
            file_log_message = f"{message}"

        if details:
            if isinstance(details, Exception):
                error_details = ''.join(traceback.format_exception(type(details), details, details.__traceback__))
                console_log_message += f"\n{Logger.COLORS[level_name]}{error_details}"
                file_log_message += f"\n{error_details}"
            else:
                formatted_details = json.dumps(details, indent=2)
                console_log_message += f"\n{Logger.COLORS['details']}{formatted_details}"
                file_log_message += f"\n{formatted_details}"

        Logger.__console_logger.log(level, console_log_message)
        if Logger.STORE_TO_FILE:
            Logger.__file_logger.log(level, file_log_message)

    @staticmethod
    def debug(message, details=None, no_meta=False):
        Logger.__log(logging.DEBUG, message, details, no_meta)

    @staticmethod
    def info(message, details=None, no_meta=False):
        Logger.__log(logging.INFO, message, details, no_meta)

    @staticmethod
    def warn(message, details=None, no_meta=False):
        Logger.__log(logging.WARNING, message, details, no_meta)

    @staticmethod
    def error(message, details=None, no_meta=False):
        Logger.__log(logging.ERROR, message, details, no_meta)

    @staticmethod
    def critical(message, details=None, no_meta=False):
        Logger.__log(logging.CRITICAL, message, details, no_meta)
