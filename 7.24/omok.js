// ? 2023년 07월 24일 과제 (1)
// ? 주제 : 자바스크립트로 오목게임 만들어보기
// ? 세부내용
// ? 1. Nodejs와 함께 콘솔창에서 실행되도록 사용자 입출력 도구를 사용한다.
// ? 2. 오목판 사이즈는 30x30으로 고정한 후 정사각형의 형태의 오목판을 만든다.
// ? 3. 사용자 입력 도구에 좌표값 (15,15)라고 입력하여 바둑돌을 둔다.
// ? 4. 흑은 1로, 백은 0으로 표기하여 화면에 흑과 백이 번갈아가면서 두도록 입력 도구가 계속 뜨도록 입력 받는다.
// ? 5. 오목 규칙에 따라 5줄이 먼저 완성되면 “Game over”와 같이 누가 이겼는지 승패를 알리는 출력을 만든다.
// ? 6. 승패가 계속 나지 않을 경우 실행 후 5분이 지나면 자동 종료시킨다.
// ? 제출 방법 : 작성된 js 파일과 추가된 js 파일 그리고 설치된 module을 메모장에 남겨 제출한다.
const readline = require('readline');

// 오목판 크기
const boardSize = 30;

// 오목판 생성
const board = [];
for (let i = 0; i < boardSize; i++) {
  const row = [];
  for (let j = 0; j < boardSize; j++) {
    row.push(null);
  }
  board.push(row);
}

// 현재 턴을 나타내는 변수 (흑: 1, 백: 0)
let currentTurn = 1;

// 콘솔 입력 도구 생성
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// 오목판 출력 함수
function printBoard() {
  for (let row = 0; row < boardSize; row++) {
    let rowStr = '';
    for (let col = 0; col < boardSize; col++) {
      if (board[row][col] === 1) {
        rowStr += '1 ';
      } else if (board[row][col] === 0) {
        rowStr += '0 ';
      } else {
        rowStr += '□ ';
      }
    }
    console.log(rowStr);
  }
  // 현재 턴이 누구인지 표시
  const turnInfo = currentTurn === 1 ? '흑' : '백';
  console.log(`${turnInfo}의 차례입니다.`);
}

// 게임 시작 함수
function startGame() {
  console.log('게임이 시작되었습니다. 좌표값을 입력하세요. (예: 15 15)');
  printBoard();

  // 5분 후 자동 종료 설정
  setTimeout(() => {
    console.log('5분이 지났습니다. 게임을 종료합니다.');

    // 현재 턴인 플레이어를 패배로 처리
    const winner = currentTurn === 1 ? '백' : '흑';
    console.log(`${winner}이 승리했습니다. "Game over"`);

    rl.close();
  }, 5 * 60 * 1000); // ! 5 * 60 * 1000(ms) = 5분

  rl.on('line', (input) => {
    const [row, col] = input.trim().split(' ').map((el) => parseInt(el, 10));

    // 입력값이 유효한지 확인
    if (row < 0 || row >= boardSize || col < 0 || col >= boardSize) {
      console.log('올바르지 않은 좌표값입니다. 다시 입력하세요.');
      return;
    }

    // 이미 돌이 놓여진 자리인지 확인
    if (board[row][col] !== null) {
      console.log('이미 돌이 놓여진 자리입니다. 다시 입력하세요.');
      return;
    }

    // 돌 놓기
    board[row][col] = currentTurn;
    // 턴 변경
    currentTurn = 1 - currentTurn;

    // 오목판 출력
    printBoard();
  });
}
// 게임 시작
startGame();