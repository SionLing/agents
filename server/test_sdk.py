# legal-agent.py
import asyncio
from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions

async def main():
    async with ClaudeSDKClient(
        options=ClaudeCodeOptions(
            system_prompt= """
            You are a Senior Product Manager with 8+ years of end-to-end internet product experience. Skilled in dissecting requirements through three core lenses—business value, user experience, and technical feasibility—you excel at identifying users’ key pain points and delivering actionable product strategies (including Roadmaps, priority matrices, and data metrics).
You possess strong cross-team communication skills to align engineering, operations, and marketing teams. When facing ambiguous requirements, you quickly clarify direction via the "user persona → scenario breakdown → value validation" framework. Responses must be concise, focused on core issues, and free of vague theories.
            """,
            allowed_tools=["Bash", "Read", "Write", "WebSearch"],
            max_turns=2
        )
    ) as client:
        # Send the query
        await client.query("Run adversarial analysis on this requirements document: pro_novel_hub.md")
        
        # Stream the response
        async for message in client.receive_response():
            if hasattr(message, 'content'):
                # Print streaming content as it arrives
                for block in message.content:
                    print(message)
                    if hasattr(block, 'text'):
                        print(block)
                        print(block.text, end='', flush=True)

if __name__ == "__main__":
    asyncio.run(main())