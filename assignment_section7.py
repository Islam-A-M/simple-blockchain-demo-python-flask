
import  json
import pickle

#1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.

waiting_for_input = True
#is_first_time=True
user_inputs=[]
def load_data():
	global user_inputs
	with open('assignmenttxt.txt', mode='rb') as f :
		    		output =f.read()
		    		user_inputs=pickle.loads(output)
load_data()
		    			
while waiting_for_input:
    print('Enter q to exit')
    print('Enter p to print all previous inputs')
    user_input = input('Enter new input: ')
    if user_input== 'q':
    	waiting_for_input=False
    	print('User left!')
    elif user_input=='p':
    			with open('assignmenttxt.txt', mode='rb') as f :
		    		output =f.read()
		    		#print(output)
		    		output_list=pickle.loads(output)
		    		
		    		
	    		for line in  output_list :
	    			print(line)
    	#2) Add another option to your user interface: The user should be able to output the data stored in            the file in the terminal.

    	#with open('assignmenttxt.txt', mode='r') as f :
#    		#output =f.read()
#    		output =f.read()
#    		#print(output)
#    		output_list=json.loads(output)
#    		print(json.loads(output))
#    		
#    		for line in  output_list :
#    			print(line)

    else:
    	
    	user_inputs.append(user_input)
    	with open('assignmenttxt.txt',mode='wb') as f :
    			f.write(pickle.dumps(user_inputs))  			
    	
    		#if not is_first_time:
    		 	  	  #user_inputs.append('\n')
    		 	  	 # f.write('\n')
    		#f.write(user_input)
    		
    		#is_first_time=False
    		#with open('assignmenttxt.txt',mode='w') as f :
#    			f.write(json.dumps(user_inputs))
			
    

#3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.

#4) Adjust the logic to load the file content to work with pickled/ json data.