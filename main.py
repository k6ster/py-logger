import time
import os

RED     = "\x1b[31;1m"
GREEN   = "\x1b[32;1m"
GRAY    = "\x1b[38;5;244m"
YELLOW  = "\x1b[33m"
PURPLE  = "\x1b[35m"
ORANGE  = "\x1b[38;5;202m"
RESET   = "\x1b[0m"

def log_suc(text: str, fields = []):
	now = time.localtime()
	current_time = time.strftime("%H:%M:%S", now)

	msg = f"{YELLOW}{current_time}{RESET} {GREEN}SUC{RESET} {text}"

	for field in fields:
		msg = f"{msg} {PURPLE}{field[0]}: {RESET}{field[1]} "

	print(msg)

def log_err(text: str, fields = []):
	now = time.localtime()
	current_time = time.strftime("%H:%M:%S", now)

	msg = f"{YELLOW}{current_time}{RESET} {RED}ERR{RESET} {text}"

	for field in fields:
		msg = f"{msg} {PURPLE}{field[0]}: {RESET}{field[1]} "

	print(msg)

def log_dbg(text: str, fields = []):
	now = time.localtime()
	current_time = time.strftime("%H:%M:%S", now)

	msg = f"{YELLOW}{current_time}{RESET} {GRAY}DBG{RESET} {text}"

	for field in fields:
		msg = f"{msg} {PURPLE}{field[0]}: {RESET}{field[1]} "

	print(msg)

def log_wrn(text: str, fields = []):
	now = time.localtime()
	current_time = time.strftime("%H:%M:%S", now)

	msg = f"{YELLOW}{current_time}{RESET} {ORANGE}WRN{RESET} {text}"

	for field in fields:
		msg = f"{msg} {PURPLE}{field[0]}: {RESET}{field[1]} "

	print(msg)
def clear_terminal():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

if __name__ == "__main__":
	log_suc("Text", [["field1", "data"], ["field2", "data"]])
	log_err("Text", [["field1", "data"], ["field2", "data"]])
	log_dbg("Text", [["field1", "data"], ["field2", "data"]])
	log_wrn("Text", [["field1", "data"], ["field2", "data"]])

