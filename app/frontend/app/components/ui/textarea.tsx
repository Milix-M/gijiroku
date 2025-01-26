type ButtonProps = Required<{
    readonly text: string;
}>;

export const Textarea = ({ text }: ButtonProps) => (

    <textarea className="w-full" value={text}></textarea>

)

export default Textarea