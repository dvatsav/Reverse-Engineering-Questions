import angr
import sys
import claripy


project = angr.Project('flippityflop')
#start_address = 0x08049bba

initial_state = project.factory.entry_state()

#passwordsize=31

#password = claripy.BVS('password', passwordsize)
#initial_state.regs.ecx = password

simulation = project.factory.simgr(initial_state)

dest_address = [0x8049BF8]
avoid_address = [0x8049DF5]




def is_successful(state):
	stdout_output = state.posix.dumps(sys.stdout.fileno())

	return "flag" in stdout_output

def should_abort(state):
	stdout_output = state.posix.dumps(sys.stdout.fileno())
	return "look right" in stdout_output

simulation.explore(find=dest_address, avoid=avoid_address)

if simulation.found:
	solution_state = simulation.found[0]

	#sol0 = solution_state.se.eval(password)
	#print sol0

	print solution_state.posix.dumps(sys.stdin.fileno())
else:
	raise Exception('Could not find the solution')