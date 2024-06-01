import Image from "next/image";

import { CodeExecutionProvider } from "./Context";

import CodeEditor from "./components/CodeEditor";
import ExecuteButton from "./components/ExecuteButton"
import SubmitButton from "./components/SubmitButton"

export default function Home() {
  return (
    <CodeExecutionProvider>
      <main className="flex min-h-screen min-w-screen flex-col items-center pt-10">
        
        <div className="justify-between">
          <ExecuteButton/>
          <SubmitButton/>
        </div>
        
        <div className="flex w-full mt-10 px-15">
          <CodeEditor/>
        </div>
      </main>
    </CodeExecutionProvider>
  );
}
