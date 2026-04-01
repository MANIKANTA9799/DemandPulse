import sys 
import traceback 
import logging 
import os

error_log_file = os.path.join("logs","errors.log")

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):#type:ignore 
        super().__init__(error_message)
        _,_,exc_tb = error_detail.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename#type:ignore
        self.line_number = exc_tb.tb_lineno#type:ignore
        self.error_message = error_message
        self.log_error()
    def log_error(self):
        error_msg = f"[ERROR] File: {self.file_name}, Line: {self.line_number}, Message: {self.error_message}"
        with open(error_log_file, "a") as f:
            f.write(error_msg + "\n")
    def __str__(self):
        return f"Error in [{self.file_name}] at line [{self.line_number}] : {self.error_message}"