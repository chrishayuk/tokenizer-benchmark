import { TimeBot } from './TimeBot';
import { NlpManager } from 'node-nlp';
import { BotConfig } from './BotConfig';

export class AsciiTimeBot extends TimeBot {
    constructor(botConfig: BotConfig, nlpManager: NlpManager) {
        super(botConfig, nlpManager);
    }

    protected handleIntent(intent: string, senderId: string, message: string): void {
        if (intent === "time.check") {
            const timezone = this.settings.timezone || 'UTC';
            const currentTime = new Date().toLocaleTimeString('en-GB', { timeZone: timezone, hour12: false });

            // Debug: Check the format of the time
            //console.log(`Current Time: ${currentTime}`);

            const asciiTime = this.convertTimeToAscii(currentTime);
            this.sendMessage(`@${senderId} The current time in ASCII art:Line 1\nLine 2"`);
            console.log(asciiTime);
        } else {
            console.log("Received non-time check message.");
        }
    }

    private convertTimeToAscii(time: string): string {
        const asciiDigits = {
            '0': [' 000 ', '0   0', '0   0', '0   0', ' 000 '],
            '1': ['  1  ', ' 11  ', '  1  ', '  1  ', ' 111 '],
            '2': [' 222 ', '2   2', '  2  ', ' 2   ', '22222'],
            '3': ['3333 ', '    3', ' 333 ', '    3', '3333 '],
            '4': ['4  4 ', '4  4 ', '44444', '   4 ', '   4 '],
            '5': ['55555', '5    ', '5555 ', '    5', '5555 '],
            '6': [' 666 ', '6    ', '6666 ', '6   6', ' 666 '],
            '7': ['77777', '   7 ', '  7  ', ' 7   ', '7    '],
            '8': [' 888 ', '8   8', ' 888 ', '8   8', ' 888 '],
            '9': [' 999 ', '9   9', ' 9999', '    9', ' 999 '],
            ':': ['     ', '  *  ', '     ', '  *  ', '     ']
        };
        

        let asciiTime = '';
        for (let i = 0; i < 5; i++) {
            let line = '';
            for (const char of time) {
                if (asciiDigits[char]) {
                    line += asciiDigits[char][i] + '  ';
                } else {
                    line += '     '; // For unsupported characters, add spaces
                }
            }
            asciiTime += line + '\n';

            // Additional Debugging
            //console.log(line);
        }

        return asciiTime;
    }
}