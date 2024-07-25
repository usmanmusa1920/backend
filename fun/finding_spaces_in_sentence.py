s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis pharetra sem mattis, porta urna eu, bibendum est. Fusce scelerisque, sapien tristique lacinia interdum, nulla enim laoreet erat, ut commodo felis turpis id massa. Morbi et malesuada eros. Integer accumsan mattis dui, eget sagittis dolor luctus vitae. Suspendisse erat augue, congue et leo non, ultrices efficitur magna. Donec sit amet neque velit. In ac metus volutpat, gravida urna ac, rhoncus erat. Nulla facilisi. Etiam nisl justo, consectetur ac libero tempor, ornare consectetur felis. Nam lacus mauris, vehicula sit amet mattis at, elementum vel dolor. Aenean at ipsum condimentum, gravida dui sed, condimentum mi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed enim nisi, accumsan id finibus sit amet, sollicitudin eu magna. Nunc sed fringilla lectus.'

if ' ' in s:
    print('\n\tThere are', int(len(s.split(' '))) - 1, 'spaces in the following sentence:\n\n"' + s + '"\n')
else:
    print('\nNo, there is no any space\n')
