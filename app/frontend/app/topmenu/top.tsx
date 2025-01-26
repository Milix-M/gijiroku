import { useState } from "react";

export function TopMenu() {
  const handleSubmit = () => {
    const file = new FormData()
    if (video) {
      file.append("file", video[0]);
      setStatus("処理しています...")
      fetch('http://localhost:5000/generate-minutes', { method: 'POST', body: file })
        .then(res => {
          res.text().then(text => {
            setMinutes(text)
          })
          setStatus("処理完了")
        })
    }
  }

  const [video, setVideo] = useState<FileList | null>();
  const [minutes, setMinutes] = useState<string>("");
  const [status, setStatus] = useState<string>("処理していません");

  return (
    <main className="flex items-center justify-center pt-8 pb-4">
      <div className="w-full max-w-xl">
        <h1 className="text-2xl text-center">議事録App</h1>

        <div className="mt-8">
          <label className="block mb-2 text-sm font-medium text-gray-900" htmlFor="filepick">Pick Video</label>
          <input accept="video/*" type="file" className="p-3 block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 " id="filepick" onChange={event => setVideo(event.target.files)} />
        </div>
        <p className="text-center">処理ステータス: {status}</p>
        <div className="mt-4 flex items-center justify-center">
          <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" onClick={() => handleSubmit()}>
            処理開始
          </button>
        </div>
        <p className="text-center mt-12">生成結果</p>
        <div className="flex items-center justify-center border rounded">
          <textarea className="w-full" defaultValue={minutes}></textarea>
        </div>
      </div>
    </main>
  );
}
