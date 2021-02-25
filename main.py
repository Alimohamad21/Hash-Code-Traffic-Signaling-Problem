from random import randint
def hc_fn(fp):
    i = 0
    streets_list = []
    t_total = 0
    intersections_count = 0
    streets_count = 0
    cars_count = 0
    bonus = 0
    car_streets_list = []
    streets_count = 0
    for line in fp:
        line = line.split()
        if not i:
            t_total = int(line[0])
            intersections_count = int(line[1])
            streets_count = int(line[2])
            cars_count = int(line[3])
            bonus = int(line[4])
        elif i < streets_count + 1:
            street = dict()
            street['intersections'] = [int(line[0]), int(line[1])]
            street['name'] = line[2]
            street['length'] = int(line[3])
            streets_list.append(street)
        else:
            car_streets = []
            for j in range(1, int(line[0]) + 1):
                car_streets.append(line[j])
            car_streets_list.append(car_streets)
        i += 1
    output_fp = open(fp.name[0] + '_output.txt', 'w')
    used_intersections_count = intersections_count
    used_intersections_list = []
    for i in range(used_intersections_count):
        used_intersection = dict()
        used_intersection['streets_count'] = 0
        used_intersection['street+green_light_time_list'] = []
        for street in streets_list:
            if street['intersections'][1] == i:
                used_intersection['street+green_light_time_list'].append([street['name'],street['length']])
                used_intersection['streets_count'] += 1
        used_intersection['id'] = i
        used_intersections_list.append(used_intersection)
    output_fp.write(f'{used_intersections_count}\n')
    for i in range(used_intersections_count):
        output_fp.write(f"{used_intersections_list[i]['id']}\n{used_intersections_list[i]['streets_count']}\n")
        for j in range(used_intersections_list[i]['streets_count']):
            output_fp.write(
                f"{used_intersections_list[i]['street+green_light_time_list'][j][0]} {used_intersections_list[i]['street+green_light_time_list'][j][1]}\n")


fps = []
fps.append(open('a.txt'))
fps.append(open('b.txt'))
fps.append(open('c.txt'))
fps.append(open('d.txt'))
fps.append(open('e.txt'))
fps.append(open('f.txt'))
for fp in fps:
    hc_fn(fp)
