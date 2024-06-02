"use client"

import React from 'react'
import { useCodeExecution } from '../Context'

const ExecutionResult: React.FC = () => {
    const {code, setCode, result, setResult} = useCodeExecution();

    return (                
        <div className="bg-zinc-900 mt-3 rounded-lg px-5 py-5">        
            <div className="mb-5">
                <h1 className="">Output</h1>                        
            </div>
            {result &&
                <div className="bg-zinc-700 py-2 px-4 rounded-lg ">
                    <pre className="text-white">{result}</pre>
                </div>
            }
            
        </div>
    )
}

export default ExecutionResult