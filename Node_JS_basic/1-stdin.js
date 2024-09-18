// 1-stdin.js

// Display welcome message and ask for name input
console.log('Welcome to Holberton School, what is your name?');

// Read input from stdin
process.stdin.on('data', (input) => {
  const name = input.toString().trim(); // Get the user's input and trim any extra whitespace
  console.log(`Your name is: ${name}`); // Display user's name

  // Close the stdin process and display closing message
  console.log('This important software is now closing');
  process.exit(); // End the program
});
