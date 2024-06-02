"use client";

import React from 'react'
import { useCodeExecution } from '../Context'

const ExecuteButton: React.FC = () => {
    const {code, setCode, result, setResult} = useCodeExecution();
    
    const handleExecute = async () => {
        console.log(JSON.stringify({"code": code}))
        const response = await fetch('http://localhost:8000/test-code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({code})
        })
        console.log("Test code req response: ", response);
        const data = await response.json();
        console.log("Test code response data: ", data);
    }

    return (
        <button onClick={handleExecute} className="p-3 text-white rounded-l-lg bg-zinc-900 mr-1">
            Test Code
        </button>
    )
}

export default ExecuteButton