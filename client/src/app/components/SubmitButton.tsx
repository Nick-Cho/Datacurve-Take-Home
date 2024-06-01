"use client";

import React from 'react'
import { useCodeExecution } from '../Context'

const ExecuteButton: React.FC = () => {
    const {code, setCode, result, setResult} = useCodeExecution();
    
    const handleSubmit = async () => {
        
    }

    return (
        <button onClick={handleSubmit} className="p-3 text-green-500 rounded-r-lg bg-zinc-900">
            Submit Code
        </button>
    )
}

export default ExecuteButton