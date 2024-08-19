import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";


const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// const analytics = getAnalytics(app);

function addData() {
    const nameInput = document.getElementById('nameInput').value;
    if (nameInput) {
        db.collection('users').add({
            name: nameInput
        })
            .then(() => {
                console.log('Doc successfully written!');
                document.getElementById('nameInput').value = '';
            })
            .catch((error) => {
                console.error("Error writing document: ", error);
            });
    } else {
        alert('Places enter a name.')
    }
}

function getData() {
    db.collection('users').onSnapshot((querySnapshot) => {
        const userList = document.getElementById('userList');
        userList.innerHTML = '';
        querySnapshot.forEach((doc) => {
            const li = document.createElement('li');
            li.textContent = doc.data().name;
            userList.appendChild(li);
        });
    });
}

getData();
