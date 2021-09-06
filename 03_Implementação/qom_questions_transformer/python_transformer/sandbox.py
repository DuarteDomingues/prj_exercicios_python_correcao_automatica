#
# history:
#
# 2020/05/13 Added sys.modules.clear() to prevent changed imported
# modules to be loaded (the no changes version was used). jbs
#
# 2020/05/13 Added log logger. jbs
#





import sys
import traceback

from io import StringIO

import logging
log = logging.getLogger(__name__)





def sandbox(code_string, filename = None):
    """Returns (sandbox_output, sandbox_error, sandbox_execption,
    sandbox_globals). (with the exception of sandbox_globals each one
    can possibly be returned as an empty string.) To mimic the output
    of the execution in the commando line with "python3 program.py"
    you should output sandbox_output and sandbox_execption
    concatenated.
    """

    old_stdout = sys.stdout
    old_stderr = sys.stderr

    captured_out = StringIO()
    captured_err = StringIO()

    sys.stdout = captured_out
    sys.stderr = captured_err

    sandbox_globals = {}
    #sandbox_locals = {} # we use exec(code, globals), with no locals
    #to mimic the execution from a file. If locals were used, the
    #class definition names would result in NameError: name '...' is
    #not defined

    sandbox_output    = ""
    sandbox_error     = ""
    sandbox_exception = ""

    # on linux compilation and execution errors go to standard error
    # we copy them do standard output to mimic IDLE 

    # clear previous imported modules. regarding imported modules code
    # string must be autonomous
    sys.modules.clear()

    try:
        if filename == None:
            code = code_string
        else:
            code = compile(code_string, filename, 'exec')

        exec(code, sandbox_globals) #, sandbox_locals)
    except:
        sandbox_exception = traceback.format_exc().splitlines()
        #print("+++++ " + str(sandbox_exception) + "+++++")
        # lines 2 and 3 refer the sandbox context
        sandbox_exception.pop(1)
        sandbox_exception.pop(1)
        sandbox_exception = "\n".join(sandbox_exception)

        log.debug('********** sandbox exception **********')
        log.debug('********** sys.path = **********')
        log.debug(sys.path)
        log.debug('********** sandbox_exception = **********')
        log.debug(sandbox_exception)
        log.debug('********** code_string = **********')
        log.debug(code_string)
        
    sandbox_output = captured_out.getvalue()
    sandbox_error  = captured_err.getvalue()

    # reset outputs to the original values
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    return (sandbox_output, sandbox_error, sandbox_exception, sandbox_globals)





if __name__ == "__main__":

    print("compilation error")
    code = "print(\"hello\") print(\"world\")"
    (out, err, excp, glbs) = sandbox(code)
    print("out  = \"" + out + "\"")
    print("err  = \"" + err + "\"")
    print("excp = \"" + excp + "\"")
    print()

    print("compilation error from a file")
    code = "print(\"hello\") print(\"world\")"
    (out, err, excp, glbs) = sandbox(code, filename = "program.py")
    print("out  = \"" + out + "\"")
    print("err  = \"" + err + "\"")
    print("excp = \"" + excp + "\"")

    print("execution error")
    code = "print(x)"
    (out, err, excp, glbs) = sandbox(code)
    print("out  = \"" + out + "\"")
    print("err  = \"" + err + "\"")
    print("excp = \"" + excp + "\"")

    print("execution error from a file")
    code = "print(x)"
    (out, err, excp, glbs) = sandbox(code, filename = "program1.py")
    print("out  = \"" + out + "\"")
    print("err  = \"" + err + "\"")
    print("excp = \"" + excp + "\"")

    print("output and execution error")
    code = "x=3\nprint(x)\nprint(y)"
    (out, err, excp, glbs) = sandbox(code)
    print("out  = \"" + out + "\"")
    print("err  = \"" + err + "\"")
    print("excp = \"" + excp + "\"")
    print()

    print("output and execution error from file")
    code = "x=3\nprint(x)\nprint(y)"
    (out, err, excp, glbs) = sandbox(code, filename = "program2.py")
    print("out  = \"" + out + "\"")
    print("err  = \"" + err + "\"")
    print("excp = \"" + excp + "\"")

