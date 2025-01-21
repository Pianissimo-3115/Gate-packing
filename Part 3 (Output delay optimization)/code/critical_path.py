from objects import *
from exception import LoopException
# dp={}
# def critical_path(input_gate:Gate,wire_delay):   #run this for all gates having only primary inputs
#     if dp.get(input_gate.id) is not None:
#         return dp[input_gate.id]
    
#     if len(input_gate.output_connections)==0:
#         dp[input_gate.id]=(input_gate.delay,[])
#         return dp[input_gate.id]

#     max_delay=0
#     pinpath=None
#     thispinpath=None
#     for pin in input_gate.pins:
#         if pin.type=="primary_output":
#             max_delay=max(max_delay,input_gate.delay)
#         elif pin.type=="secondary_output":
#             for connection in pin.connections:
#                 critpath=critical_path(connection[0],wire_delay)
#                 if max_delay<critpath[0]+input_gate.delay+pin.network.wire_length*wire_delay:
#                     max_delay=critpath[0]+input_gate.delay+pin.network.wire_length*wire_delay
#                     pinpath=critpath[1]
#                     thispinpath=(pin,connection[1])
#     # pinpath.append(thispinpath)
#     pinpath=[thispinpath]+pinpath
#     dp[input_gate.id]=(max_delay,pinpath)
#     return dp[input_gate.id]

 



def critical_path(input_gate: Gate, wire_delay,dp):
    stack = [(input_gate, None)]
    while stack:
        current_gate, parent_info = stack[-1]
        
        if current_gate.id in dp:
            stack.pop()
            continue
            
        if len(current_gate.output_connections) == 0:
            dp[current_gate.id] = (current_gate.delay, [])
            stack.pop()
            continue
            
        all_processed = True
        for pin in current_gate.pins:
            if pin.type == "secondary_output":
                for connection in pin.connections:
                    if connection[0].id not in dp:
                        stack.append((connection[0], (pin, connection[1])))
                        if len(stack)>1000:
                            raise LoopException("Given gates contain an infinite loop")
                        all_processed = False
                        break
            if not all_processed:
                break
                
        if all_processed:
            max_delay = 0
            pinpath = []
            
            for pin in current_gate.pins:
                if pin.type == "primary_output":
                    max_delay = max(max_delay, current_gate.delay)
                elif pin.type == "secondary_output":
                    for connection in pin.connections:
                        critpath = dp[connection[0].id]
                        total_delay = (critpath[0] + current_gate.delay + pin.network.wire_length * wire_delay)
                        if max_delay < total_delay:
                            max_delay = total_delay
                            pinpath = [(pin, connection[1])] + critpath[1]
            
            dp[current_gate.id] = (max_delay, pinpath)
            stack.pop()
    
    return dp[input_gate.id]
















