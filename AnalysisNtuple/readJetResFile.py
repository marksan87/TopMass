inputFile = open("Spring16_25nsV10_MC_PtResolution_AK4PFchs.txt","read")


Values = {}

for line in inputFile:
    if '{' in line: continue

    tmp = line.split()
    line_values = [eval(x) for x in tmp]

    if not (line_values[0],line_values[1]) in Values:
        Values[(line_values[0],line_values[1])] = {}

    Values[(line_values[0],line_values[1])][(line_values[2],line_values[3])] = line_values[7:]
    
etaBands =  Values.keys()
etaBands.sort()

rhoBands = Values[etaBands[0]].keys()
rhoBands.sort()


for eta in etaBands:
    print 'if ( eta > %.1f && eta < %.1f ) {' % eta
    for rho in rhoBands:
        print '\tif ( rho > %.1f && rho < %.1f ) {' % rho,
        print 'p0 = %f; p1 = %f; p2 = %f; p3 = %f; }'% tuple(Values[eta][rho])
    print '}'
