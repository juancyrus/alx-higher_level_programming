#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments"""
    import sys

    def print_arguments():
      count = len(sys.argv) - 1
      plural_s = 's' if count != 1 else ''
      
      print(f"Number of argument{plural_s}: {count}{'.' if count == 0 else ':'}")

      for i, arg in enumerate(sys.argv[1:], start=1):
         print(f"{i}: {arg}")
