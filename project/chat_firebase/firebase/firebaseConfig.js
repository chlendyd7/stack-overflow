import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.4.0/firebase-app.js';
import { getDatabase, ref, push, set, onValue } from 'https://www.gstatic.com/firebasejs/10.4.0/firebase-database.js';

// Firebase 설정 객체


// Firebase 초기화
const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

// db를 다른 모듈에서 사용할 수 있도록 내보내기
export { db, ref, push, set, onValue };
