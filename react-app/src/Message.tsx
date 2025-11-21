import { useEffect, useState } from "react";

function Message() {
    const [text, setText] = useState("")
    useEffect(() => {
        const load = () => {
            fetch("/output.txt")
            .then(res => res.text())
            .then(data => setText(data))
        }
    load();

    const interval = setInterval(load, 1000)

    return () => clearInterval(interval)
    }, [])

    return <h1>{text}</h1>
}

export default Message;