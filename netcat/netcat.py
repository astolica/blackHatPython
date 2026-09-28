import argparse
import socket 
import shlex 
import subprocess
import sys 
import textwrap
import threading 

def execute(cmd):
    cmd = cmd.strip()
    