import pandas

data = pandas.read_excel('/Users/FabianFalck/Documents/[02] Management Systems Simulation/[01] Assignments/2/barber_data.xlsx')
data.values[:,1]

for row in data.values:
    print row[1]

print data

class Customer:
    def __init__(self, id, at, iat, sd):
        self.id = id
        self.at = at # arrival time
        self.iat = iat #interarrival time
        self.sd = sd #service duration
        self.sbt = -1 #service begin time
        self.dt = -1 #departure time
        self.wt = -1 #waiting time
        self.ct = -1 # cycle time

#generate data

customers = []
def init(data):
    for row in data.values:
        customer = Customer(row[0], row[1], row[2], row[3])
        customers.append(customer)
    return customers

customers = init(data)


customer_test = customers

len(customer_test)
for customer in customer_test:
    print customer.id


def sorto(customer):
    return customer.at


customers_test_sorted = sorted(customer_test, key = sorto, reverse=True)

print len(customers_test_sorted)
for customer in customers_test_sorted:
    print customer.at


def sorto_sd(customer):
    return customer.sd

#generate data end

def scheduling(customers_input):

    customers_ns = customers_input[:] # not served yet
    customers_s = [] # already served yet
    customers_a = [] #arrived customers who want to be served

    print 'here'
    print len(customers_ns)
    for c in customers_ns:
        print c.at

    customers_a.append(customers_ns.pop())
    system_time = 0
    lock_time = 0



    while(len(customers_s)<10):
        #if no one has arrived and the system is waiting
        if len(customers_a)==0:
            help = sorted(customers_ns,  key=sorto, reverse=True) #find the next customer to arrive
            c = help.pop()
            customers_ns.remove(c)
            lock_time = lock_time + c.at - system_time
            system_time = c.at
            current_customer = c
        else:

            print 'customer_ns' + str(len(customers_ns))
            print 'customer_a' + str(len(customers_a))
            print 'arrived' + str(len(customers_a))

            customer_a_sorted = sorted(customers_a[:], key=sorto_sd, reverse = True)
            current_customer = customer_a_sorted.pop() #is the customer with the smallest sd
            customers_a = customer_a_sorted #don't forget man!!!!

        print current_customer.id

        current_customer.sbt = system_time
        current_customer.dt = system_time + current_customer.sd
        current_customer.wt = system_time - current_customer.at
        current_customer.ct = current_customer.dt - current_customer.at
        customers_s.append(current_customer)

        system_time = system_time + current_customer.sd

        for customer in customers_ns:
            if customer.at <= system_time:
                save = customer
                customers_ns.remove(customer)
                customers_a.append(save)

    print 'lock-time: ' + str(lock_time)
    return customers_s





output = scheduling(customers_test_sorted)
len(output)

help = []
for c in output:
    #print c.__dict__
    help.append(c.__dict__)

df = pandas.DataFrame(help)
df


pandas.DataFrame.to_excel(df,excel_writer='/Users/FabianFalck/Documents/[02] Management Systems Simulation/[01] Assignments/2/final.xlsx')


#generating a list of arrivals and departures:

df[['id','at','dt']]

sequences = []
for index, row in df.iterrows():
    sequences.append((row['id'],row['at'], 'Arrival'))
    sequences.append((row['id'], row['dt'], 'Departure'))

def sort_tuple(tuple):
    return tuple[1]

sequences_sorted = sorted(sequences, key = sort_tuple)

#get it into a file

result_string = ''
for tuple in sequences_sorted:
    result_string = result_string + str(tuple[0]) + ', '+ str(tuple[1]) + ', '+ str(tuple[2]) + '\n'

print result_string

file = open('/Users/FabianFalck/Documents/[02] Management Systems Simulation/[01] Assignments/2/sequences.txt', 'w')
file.write(result_string)
file.close()

