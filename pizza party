pizzas_purchased = int(input('Number of pizzas purchased : '))
slices_per_pizza = int(input('Number of slices per pizza : '))
adults = int(input('Number of adults : '))
children = int(input('Number of children : '))

slices_per_adult = adults * 2
slice_total = pizzas_purchased * slices_per_pizza
slices_per_child = (slice_total - slices_per_adult) // children
slices_left_over = (slice_total - slices_per_adult) % children 

print('Number of slices each child will get is : ', slices_per_child)
print('Number of slices left over is : ', slices_left_over)
