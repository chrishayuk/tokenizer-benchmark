import { BaseBot } from '../BaseBot';
import { NlpManager } from 'node-nlp';
import { BotConfig } from '../BotConfig';

export class UnixTimeBot extends BaseBot {
    // constructor
    constructor(botConfig: BotConfig, nlpManager: NlpManager) {
        // call base class
        super(botConfig.name, botConfig.type, botConfig.description, botConfig.settings, nlpManager, botConfig.welcomeMessage);
    }

    // handle the intent
    protected handleIntent(intent: string, senderId: string, message: string): void {
        // looks for a time check
        if (intent === "unix.time.check" || intent === "time.check") {
            // get the current unix time
            const unixTime = Math.floor(Date.now() / 1000);

            // send the current time to the sender
            this.sendMessage(`@${senderId} The current Unix time is: ${unixTime}`);
        } else {
            console.log("Received non-unix time check message.");
        }
    }
}