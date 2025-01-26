type ButtonProps = Required<{
    readonly text: string;
}>;

export const Button = ({ text }: ButtonProps) => (
    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">
        {text}
    </button>
)

export default Button