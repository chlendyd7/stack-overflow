import { doc, getDoc, setDoc } from "https://www.gstatic.com/firebasejs/9.12.1/firebase-firestore.js";
import { db } from './firestore_config.js';



export async function getData() {
    const citiesRef = collection(db, "cities");
    const docRef = doc(db, "cities", "SF");
    const docSnap = await getDoc(docRef);

    if (docSnap.exists()) {
        console.log("Document data:", docSnap.data());
        return docSnap.data();
    } else {
        console.log("No such document!");
        return null;
    }
}

export async function setData() {
    const docRef = doc(db, "cities", "SF");
    const data = {
        test: {
            name: "buggerking",
            discount: 3000
        },
        name: "San Francisco",
        state: "CA",
        country: "USA"
    };

    await setDoc(docRef, data);
    console.log("Document written with ID: SF");
}