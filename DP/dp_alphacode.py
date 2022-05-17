# cook your dish here


dp = {}

def f(inp_str):
    if inp_str[0] == '0':
        return 0
    if len(inp_str) <= 2:
        int_inp_str = int(inp_str)
        if int_inp_str > 10 and int_inp_str < 27 and int_inp_str != 20:
            retval = 2
        else:
            retval = 1
        dp[inp_str] = retval
        return retval
        
    elif inp_str in dp:
        return dp[inp_str]
    
    else:
        if int(inp_str[:2]) < 27 and int(inp_str[:2]) > 10 and int(inp_str[:2]) != 20:
            dp[inp_str] = f(inp_str[1:]) + f(inp_str[2:]) 
        elif int(inp_str[:2]) == 20 or int(inp_str[:2]) == 10 :
            dp[inp_str] = f(inp_str[2:])
        else:
            dp[inp_str] = f(inp_str[1:])
        # print(dp, inp_str)
        return dp[inp_str]
    


if __name__ =='__main__':
    usr_inp = ['910718121248837563131011010562148997157871108610896449481048985210110996954824911081010','324','6']

    print(f(usr_inp[0]))
    print(f(usr_inp[1]))
    print(f(usr_inp[2]))
    # print(dp)
    