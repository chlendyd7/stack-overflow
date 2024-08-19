const ChatRef = collection(db, 'Chats')



export async function setChatData() {
    await setDoc(doc(citiesRef, ""))
}