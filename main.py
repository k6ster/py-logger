import time

RED     = "\x1b[31;1m"
GREEN   = "\x1b[32;1m"
GRAY    = "\x1b[38;5;244m"
YELLOW  = "\x1b[33m"
PURPLE  = "\x1b[35m"
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
