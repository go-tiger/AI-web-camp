// ? 2023년 07월 24일 과제 (2)
// ? 주제 : null과 undefined의 차이점을 찾아보기
// ? 세부내용
// ? 1. 어떨때 값이 null이 되고 undefined으로 저장되는지 가능한 모든 케이스의 js 코드를 작성한다.
// ? 2. 각 케이스의 코드상에 저장된 변수가 왜 null이고 undefined인지 원인을 설명한다.
// ? 3. 비교연산자를 활용하여 각각의 케이스에 따라 null인지 undefined인지 확인하는 코드를 작성한다.
// ? 제출 방법 : 작성된 js 파일과 내용을 설명할 수 있는 텍스트를 주석을 활용하여 기입한다.

// TODO: 1. 어떨때 값이 null이 되고 undefined으로 저장되는지 가능한 모든 케이스의 js 코드를 작성한다.
// TODO: 2. 각 케이스의 코드상에 저장된 변수가 왜 null이고 undefined인지 원인을 설명한다.
// * 케이스 1: 변수를 선언만 하고 값 할당 안하면 undefined
let null_undefined_case_one;
console.log("케이스 1:", null_undefined_case_one);

// * 케이스 2: 변수에 명시적으로 undefined 값을 할당
let null_undefined_case_two = undefined;
console.log("케이스 2:", null_undefined_case_two);

// * 케이스 3: 변수에 null 값을 할당
let null_undefined_case_three = null;
console.log("케이스 3:", null_undefined_case_three);

// * 케이스 4: 함수에서 return 문이 없거나 명시적으로 undefined를 반환할때
function null_undefined_case_four() {
  return; // ! return이 없어도 undefined를 반환함
}
console.log("케이스 4:", null_undefined_case_four());

// * 케이스 5: 함수에서 명시적으로 null을 반환할때
function null_undefined_case_five() {
  return null;
}
console.log("케이스 5:", null_undefined_case_five());

// * 케이스 6: 객체에 없는 값 undefined
const obj = {};
console.log("케이스 6:", obj.case6);

// * 케이스 7: 배열에 없는 인덱스 undefined
const arr = [];
console.log("케이스 7:", arr[0]);

// TODO: 3. 비교연산자를 활용하여 각각의 케이스에 따라 null인지 undefined인지 확인하는 코드를 작성한다.
function chk_null_undefined(Value) {
  if (Value === null) {
    console.log("null");
  } else {
    console.log("undefined");
  }
}

chk_null_undefined(null_undefined_case_one); // * undefined
chk_null_undefined(null_undefined_case_two); // * undefined
chk_null_undefined(null_undefined_case_three); // * null
chk_null_undefined(null_undefined_case_four()); // * undefined
chk_null_undefined(null_undefined_case_five()); // * null
chk_null_undefined(obj.case6); // * undefined
chk_null_undefined(arr[0]); // * undefined