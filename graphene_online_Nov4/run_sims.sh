#!/usr/bin/env bash

for i in 1 2 3 4 5
do
  export PARSE_COUNT=$i
  sed -i.bak -r 's/input_from_shell/'$i'/' in.efield_modified_2
  mpirun -np 4 lmp_mpi -in in.efield_modified_2
  python3 -c 'import dump_parse; dump_parse'
  cp -f in.efield_modified_2.bak in.efield_modified_2
done

rm -r in.efield_modified_2.bak