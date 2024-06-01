"use client";

import React from 'react'
import { useCodeExecution } from '../Context'

const ExecuteButton: React.FC = () => {
    const {code, setCode, result, setResult} = useCodeExecution();
    
    const handleExecute = async () => {
        
    }

    return (
        <button onClick={handleExecute} className="p-3 text-white rounded-l-lg bg-zinc-900 mr-1">
            Test Code
        </button>
    )
}

export default ExecuteButton