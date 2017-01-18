def gender_display(gen = 'Unknown'):
    if gen is 'm':
         gen = 'Male'

    elif gen is 'f':
         gen = 'Female'

    print (gen)

#driver function
if __name__ == "__main__":
    gen1 = 'm'
    gen2 = 'f'
    gender_display(gen1)
    gender_display(gen2)
    gender_display()
