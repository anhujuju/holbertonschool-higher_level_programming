#!/usr/bin/node
// JS prints a message depending of the number of arguments passed

if (process.argv[3]) {
    console.log('Arguments found');
  } else if (process.argv[2]) {
    console.log('Argument found');
  } else {
    console.log('No argument');
  }
