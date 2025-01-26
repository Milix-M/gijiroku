import type { Route } from "./+types/home";
import { TopMenu } from "../topmenu/welcome";

export function meta({ }: Route.MetaArgs) {
  return [
    { title: "議事録App" },
    { name: "description", content: "議事録を生成します" },
  ];
}

export default function Home() {
  return <TopMenu />;
}
