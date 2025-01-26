import Button from "../components/ui/button";
import Textarea from "../components/ui/textarea";

export function TopMenu() {
  return (
    <main className="flex items-center justify-center pt-8 pb-4">
      <div className="w-full max-w-xl">
        <h1 className="text-2xl text-center">議事録App</h1>

        <div className="mt-8 flex items-center justify-center "><Button text="動画を選択" /></div>
        <p className="text-center mt-12">生成結果</p>
        <div className="flex items-center justify-center border rounded">
          <Textarea text="aaaaaaaaaaaaaa" />
        </div>
      </div>
    </main>
  );
}
