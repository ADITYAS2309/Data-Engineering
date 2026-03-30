
// Defining variables

// Use let to define variab;e
// Can be reassigned w/o need to mention let again
// String, number, boolean, undefined, null are some of types
let y;
console.log(y); // Shows undefined on console
let x = 'Adi';
console.log(x);

// Defining constants
// Can't be reassigned once declared
const val = 'Fixed value';
console.log(val);

// Defining objects
// Can store different data type objects in array
let person = {
    name: 'Aditya Sangave',
    age: 24
};
person.gender = 'Male';
console.log(person.name);
console.log(person.age);
console.log(person.gender);

// Defining Arrays
let arr = ['Red', 'BLue', 'Green'];
arr[3] = 'Black'
console.log(arr);
console.log(arr[3]);
console.log(arr.length);

// Functions:
function add(a,b){
    return a+b
}
let output = add(a = 5, b = 2);
console.log(output);
console.log(add(3,2));
