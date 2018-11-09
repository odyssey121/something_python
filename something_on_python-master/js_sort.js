var names = ["lexa", "dima", "anton", "andrey", "pasha", "kiril"],
  humans = [];
function Human(name, age, height) {
  this.name = name;
  this.age = age;
  this.height = height;
}
function rand(n, m) {
  return Math.round(Math.random() * (m - n) + n);
}
for (let i = 0; i < names.length; i++) {
  humans[i] = new Human(
    names[i],
    rand(14, 55),
    rand(155, 200)
  );
}
function mysort(prop){
  return function(obj1,obj2){
    return obj2[prop] - obj1[prop];
  };
}
console.log(humans.sort(mysort('age')));
console.log(window.history);
console.log(window);
for (i = 0; names.length > i; i++){
  document.write('<p>'+names[i]+'<\p>');
}