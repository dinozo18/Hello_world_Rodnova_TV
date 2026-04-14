#!/bin/bash
df -h | awk 'NR > 1 {
    filesystem = $1
    use_percent = $5
    gsub(/%/, "", use_percent)
    printf "%-30s %8s\n", filesystem, $5
    if (use_percent > 90) {
        print "⚠️  ПРЕДУПРЕЖДЕНИЕ: " $1 " заполнена на " $5 "!"
        print ""
    }
}'
