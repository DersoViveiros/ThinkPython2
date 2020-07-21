import time

def time_now():
    t = time.time() #time in seconds since the epoch
    day = 24*60*60 #one day in seconds
    days_since_ep = int(t//day)
    hours = int((t - days_since_ep*24*60*60)//(60*60))
    mins = int((t-days_since_ep*24*60*60 - hours*60*60)//60)
    secs = int((t-days_since_ep*24*60*60 - hours*60*60-mins*60))
    print('It passed {} days, {} hours, {} minutes and {} seconds since the epoch'.format(days_since_ep,hours,mins,secs))

time_now()