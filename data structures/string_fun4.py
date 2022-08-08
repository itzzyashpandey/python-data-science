name=input("what's yor name = ")

print(name)
print(f"length: {len(name)}")

cl_name= name.strip() #remove leading and trailing zero

print(cl_name)
print(f"length: {len(cl_name)}")

secret_msg='00000000000SD000000000'
print(secret_msg.strip('0'))
print(secret_msg.lstrip('0'))
print(secret_msg.rstrip('0'))

crap_msg='''                                                                                
                                     hey bro                                                      
                                                                                           '''
clean_msg=crap_msg.strip()
print(clean_msg)
print(f"lenngth of msg: {len(clean_msg)}")                                                                                           