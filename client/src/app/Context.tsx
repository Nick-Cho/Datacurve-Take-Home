"use client";
import React, { createContext, useState, useContext, ReactNode } from 'react';

interface CodeExecutionContextProps {
    code: string;
    setCode: (code: string) => void;
    result: string;
    setResult: (result: string) => void;
}

const CodeExecutionContext = createContext<CodeExecutionContextProps | undefined> (undefined);

export const useCodeExecution = () => {
    const context = useContext(CodeExecutionContext);
    if (context === undefined) {
        throw new Error('useCodeExecution must be used within a CodeExecutionProvider');
    }
    return context;
};
export const CodeExecutionProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
    const [code, setCode] = useState<string>('');
    const [result, setResult] = useState<string>(''); 
    
    return (
      <CodeExecutionContext.Provider value={{ code, setCode, result, setResult}}>
        {children}
      </CodeExecutionContext.Provider>
    );
};

