import sys

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
    def __init__ (self):
        self.first = None

    # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        new_link = Link(coeff, exp)
        previous = self.first
        current = self.first
        # catch empty lists
        if (current == None) or (int(new_link.exp) >= int(current.exp)):
            new_link.next = self.first
            self.first = new_link
            return
        # traverse linked list
        while (int(current.exp) > int(new_link.exp)):
            # catch cases where link needs to inserted last
            if (current.next == None):
                current.next = new_link
                return
            previous = current
            current = current.next
        # insert new_link between previous and current
        previous.next = new_link
        new_link.next = current

    # reduce polynomial so that terms with same coefficient are added
    def reduce(self):
        previous = self.first
        # catch empty linked lists and lists with only one link
        if (previous == None) or (previous.next == None):
            return
        current = previous.next
        # traverse the linked list
        while (current != None):
            # find terms with same exp
            if (previous.exp == current.exp):
                # add the coefficients
                previous.coeff = int(previous.coeff) + int(current.coeff)
                # delete current link from linked list
                previous.next = current.next
                # update pointer
                current = current.next
            else: 
                previous = current
                current = current.next
    
    # remove links with 0 coeff
    def remove_0(self):
        previous = self.first
        # catch empty lists
        if (previous == None):
            return
        # remove 0s from beginning of list
        while (int(previous.coeff) == 0):
            self.first = previous.next
            previous = self.first
        # traverse through rest of list
        current = self.first
        while (current != None):
            if (int(current.coeff) == 0):
                previous.next = current.next
                current = current.next
            else: 
                previous = current
                current = current.next
        
    # add polynomial p to this polynomial and return the sum
    def add (self, p):
        # create a new linked list to hold the sum
        sum = LinkedList()
        # copy links from self into sum
        current = self.first
        while (current != None):
            sum.insert_in_order(current.coeff, current.exp)
            current = current.next
        # copy links from p into sum
        pcurrent = p.first
        while (pcurrent != None):
            sum.insert_in_order(pcurrent.coeff, pcurrent.exp)
            pcurrent = pcurrent.next
        # reduce the sum and return
        sum.reduce()
        sum.remove_0()
        return sum

    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        # create new linked list to hold product
        product = LinkedList()
        # traverse though self
        current = self.first
        while (current != None):
            pcurrent = p.first
            # traverse linked list p
            while (pcurrent != None):
                # calculate new coeff and new exp
                new_coeff = int(current.coeff) * int(pcurrent.coeff)
                new_exp = int(current.exp) + int(pcurrent.exp)
                product.insert_in_order(new_coeff, new_exp)
                pcurrent = pcurrent.next
            current = current.next
        # reduce the product and return
        product.reduce()
        product.remove_0()
        return product

    # create a string representation of the polynomial
    def __str__ (self):
        string = ''
        current = self.first
        # catch empty lists
        if (current == None):
            return string
        # traverse linked list
        while (current.next != None):
            string += f'{str(current)} + '
            current = current.next
        string += str(current)
        return string

def main():
    # read data from file poly.in from stdin
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].split(' ')

    # create polynomial p
    p = LinkedList()
    for i in range(1, int(lines[0][0]) + 1):
        if (len(lines[i]) == 2):
            p.insert_in_order(lines[i][0], lines[i][1])

    # create polynomial q
    q = LinkedList()
    for i in range(int(lines[0][0]) + 3, len(lines)):
        if (len(lines[i]) == 2):
            q.insert_in_order(lines[i][0], lines[i][1])

    # get sum of p and q and print sum
    sum = p.add(q)
    print(sum)

    # get product of p and q and print product
    product = p.mult(q)
    print(product)

if __name__ == "__main__":
    main()