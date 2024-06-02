"use client";

import React from 'react'
import { useCodeExecution } from '../Context'

import Editor from 'react-simple-code-editor';

import {highlight, languages} from 'prismjs/components/prism-core';
import 'prismjs/components/prism-python';
import 'prismjs/themes/prism.css';

import ExecutionResult from './ExecutionResult';
const CodeEditor: React.FC = () => {
    const {code, setCode, result, setResult} = useCodeExecution();

    return (
        <div className="flex flex-col w-full">
            <Editor
                value = {code}
                onValueChange={code => setCode(code)}
                highlight={code => highlight(code, languages.python, "python")}
                padding={10}
                className = "code-editor"
            >
            </Editor>
            <ExecutionResult/>
        </div>
    )
}

export default CodeEditor