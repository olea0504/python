def calculate_change(payment, cost):
    
    change = payment - cost
    remainder = change // 50000
   
    print ("%d원 지폐 : %d장" % (50000, remainder))
    
    change = change - (50000 * (remainder))
    remainder = change // 10000
    
    print ("%d원 지폐 : %d장" % (10000, remainder))
  
    change = change - (10000 * (remainder))
    remainder = change // 5000
    
    print ("%d원 지폐 : %d장" % (5000, remainder))
      
    change = change - (5000 * (remainder))
    remainder = change // 1000
    
    print ("%d원 지폐  : %d장" % (1000, remainder))
    
    

    
    
# test
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
