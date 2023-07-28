set terminal png
set output "throughput graph.png"
set title "Throughput vs time"
set xlabel "Time (Seconds)"
set ylabel "Throughput"
plot "output.txt" using 1:2 with linespoints title "Throughput vs time"

set terminal png
set output "averagedelaygraph.png"
set title "averagedelay vs time"
set xlabel "Time (Seconds)"
set ylabel "Throughput"
plot "output.txt" using 1:3 with linespoints title "averagedelayvs time"

